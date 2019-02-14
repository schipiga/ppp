import argparse

import ppp


def main():
    parser = argparse.ArgumentParser(description="Grab web links")
    parser.add_argument(
        "uri", metavar="uri", type=str,
        help="URI to retrieve links from")
    parser.add_argument(
        "--as", type=str, default="text",
        choices=["text", "html", "json", "yaml"],
        help="Result format type (text by default)")
    parser.add_argument(
        "--enum", action="store_true",
        help="Add enumation for links (for text and html only)")
    args = parser.parse_args()

    opts = {}
    if getattr(args, "as") in ("html", "text"):
        opts["enum"] = args.enum

    print(getattr(ppp, "links_as_" + getattr(args, "as"))(args.uri, **opts))
