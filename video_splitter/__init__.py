import json
import os

from helpers import slugify


class VideoSplitter:
    def __init__(self, meta_path: any):
        self.meta_file = open(meta_path)
        self.meta_path = meta_path

    def compute(self):
        """Split videos with the specified metadata."""
        meta = json.load(self.meta_file)['videos']

        for i, video in enumerate(meta):
            video_parts = video['parts']
            video_in_path = video['in_path']
            destination_path = video['destination_path']
            out_extension = video['out_extension']

            if not os.path.exists(video_in_path):
                raise Exception(f'Input video with the path {video_in_path} does not exist')

            if not os.path.exists(destination_path):
                os.mkdir(destination_path)

            for j, part in enumerate(video_parts):
                start = part['start']
                end = part['end']
                title = part['title']

                cmd = ['ffmpeg', '-y', '-ss', start, '-to', end, '-i', video_in_path, '-c', 'copy', f'{destination_path}/{slugify(title)}.{out_extension}']
                print(' '.join(cmd))
                os.system(' '.join(cmd))

        self.meta_file.close()


        