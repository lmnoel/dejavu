import dejavu.fingerprint as fingerprint
import dejavu.decoder as decoder
import time


class FileRecognizer:

    def __init__(self, dejavu):
        self.dejavu = dejavu
        self.Fs = fingerprint.DEFAULT_FS

    # TODO: multiproc this
    def _recognize(self, group_id, known_song_id, channels, sample_rate):
        matches = []
        for channel in channels:
            matches.extend(self.dejavu.find_matches(group_id, known_song_id, channel, sample_rate))
        return self.dejavu.align_matches(matches)

    def recognize_file(self, filename, group_id, known_song_id):
        channels, sample_rate, file_hash = decoder.read(filename, self.dejavu.limit)

        t = time.time()
        match = self._recognize(group_id, known_song_id, channels, sample_rate)
        t = time.time() - t

        if match:
            match['match_time'] = t

        return match

    def recognize(self, filename, group_id, known_song_id):
        return self.recognize_file(filename, group_id, known_song_id)


