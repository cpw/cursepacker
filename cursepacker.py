import json
import sys
import zipfile

import requests
import argparse
import re
import os
import os.path
import shutil

packurlmatcher = re.compile(r"""https://www.curseforge.com/minecraft/modpacks/(?P<packname>[\S]+)/download/(?P<dlcode>[\d]+)""")
sess = requests.session()
sess.headers = {
    'User-Agent': 'My User Agent 1.0'
}

def getpackzip():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    args = ap.parse_args()
    print(type(args.url))
    packmatch = packurlmatcher.match(args.url)
    if packmatch is None:
        print("Invalid pack URL")
        sys.exit(1)
    dlcode = packmatch.groupdict()["dlcode"]
    print("Downloading slug {}".format(packmatch.groupdict()['packname']))
    url = r"""https://addons-ecs.forgesvc.net/api/v2/addon/0/file/{}/download-url""".format(dlcode)
    packurl = sess.get(url).text
    filename = downloadfile(packurl, packurl[packurl.rindex("/")+1:])
    target = filename[:-4]
    if os.path.exists(target):
        shutil.rmtree(target+".bak", ignore_errors=True)
        os.rename(target, target+".bak")

    with zipfile.ZipFile(filename) as zf:
        zf.extractall(target)

    os.rename(os.path.join(target, "overrides"), os.path.join(target, "minecraft"))
    with open(os.path.join(target,"manifest.json")) as manifestfile:
        manifest = json.load(manifestfile)
        for f in manifest['files']:
            downloadentry(f, os.path.join(target, "minecraft", "mods"))

def downloadentry(entry, outdir):
    fileinfo = r"""https://addons-ecs.forgesvc.net/api/v2/addon/{}/file/{}""".format(entry['projectID'], entry['fileID'])
    info = sess.get(fileinfo).json()
    print("Downloading {}".format(info['displayName']))
    downloadfile(info['downloadUrl'], os.path.join(outdir, info['fileName']))

def downloadfile(url, localfile):
    with sess.get(url, stream=True) as r:
        r.raise_for_status()
        with open(localfile, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
    return localfile


getpackzip()
