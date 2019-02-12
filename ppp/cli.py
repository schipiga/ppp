import argparse

import ppp


def main():
    parser = argparse.ArgumentParser(description="Grab web links")
    parser.add_argument("uri", metavar="uri", type=str)
    parser.add_argument(
        "--as", type=str, default="text",
        choices=["text", "html", "json", "yaml"])
    parser.add_argument("--enum", action="store_true")
    args = parser.parse_args()

    opts = {}
    if getattr(args, "as") in ("html", "text"):
        opts["enum"] = args.enum

    print(getattr(ppp, "links_as_" + getattr(args, "as"))(args.uri, **opts))
