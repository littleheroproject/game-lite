#!/usr/bin/env bash
if [ -d mdbook ]; then
    rm -rf mdbook
fi
mkdir mdbook
cd mdbook

if [ "$(uname)" == "Darwin" ]; then
    download_url="https://github.com/rust-lang/mdBook/releases/download/v0.4.10/mdbook-v0.4.10-x86_64-apple-darwin.tar.gz"
else
    download_url="https://github.com/rust-lang/mdBook/releases/download/v0.4.10/mdbook-v0.4.10-x86_64-unknown-linux-gnu.tar.gz"
fi

wget "$download_url" -O mdbook.tgz
tar -zxvf mdbook.tgz

rm mdbook.tgz
