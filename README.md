This is a little script to split multiple videos with simplicity.

`ffmpeg` is required.

```
$ python main.py -h

Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -p PATHNAME, --path=PATHNAME
                        JSON metadata file pathname
```

## Metadata structure

To split videos, we have to create a JSON metadata file with the following structure.

```json
[
    "videos" : [
        {
            "in_path": "IN_PATH",
            "destination_path": "DESTINATION_PATH",
            "out_extension": "OUT_EXTENSION",
            "parts": [
                {
                    "start": "00:00:00",
                    "end": "00:05:00",
                    "title": "First"
                },
                {
                    "start": "00:05:01",
                    "end": "00:10:00",
                    "title": "Second"
                }
            ]
        }
    ]
]
```

- `videos`: Videos metadata
    - `in_path` : Path of the target video
    - `destination_path` : Destination of the output(s)
    - `out_extension` : Extension of the output(s)
    - `parts` : Splitting interval
        - `start`: Start time
        - `end`: End time
        - `title`: Split title
