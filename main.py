from optparse import OptionParser

from video_splitter import VideoSplitter


def main():
    parser = OptionParser()

    parser.add_option(
        '-p',
        '--path',
        dest='pathname',
        help='videos metadata pathname.',
        type='string',
        action='store'
    )

    opts, args = parser.parse_args()

    if opts.pathname:
        vp = VideoSplitter(opts.pathname)
        vp.compute()


if __name__ == '__main__':
    main()
    