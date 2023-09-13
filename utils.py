import re
import unicodedata


def slugify(v, allow_unicode=False) -> str:
    """
        Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
        dashes to single dashes. Remove characters that aren't alphanumerics,
        underscores, or hyphens. Convert to lowercase. Also strip leading and
        trailing whitespace, dashes, and underscores.

        :param v: The string to be converted.
        :param allow_unicode: If True, don't convert to ASCII.

        :return: The slug.
        """
    v = str(v)
    if allow_unicode:
        v = unicodedata.normalize('NFKC', v)
    else:
        v = unicodedata.normalize('NFKD', v).encode('ascii', 'ignore').decode('ascii')
        v = re.sub(r'[^\w\s-]', '', v.lower())
        return re.sub(r'[-\s]+', '-', v).strip('-_')
    