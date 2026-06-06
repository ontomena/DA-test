---
layout: post
title: "xyberphon"
date: 2026-06-06
categories: [sound]
tags: [projects, research]
image: /assets/images/xyberphon-thumb.jpg
excerpt: "A tuneful resurrection from the past web archives"
---
# xyberphon resurrection
In the misty days of 1999, or thereabouts, I used to spend a lot of time messing about with tools like Dreamweaver and Flash---a great pairing for creating loads of outlandish web elements back in the day. 

One of the things I came up with that seemed to go down pretty well at the time was the xyberphon. It's been a while since the .swf files output by Flash stopped working (2020) and gradually the whole Macromedia culture dispersed...

But... now it is possible to bring such things back from the dead. Here's how I did it--with a little bit of help from Claude ;-)

- Unpacked the SWF — parsed the binary format directly to inventory exactly what was inside the original (tag types, stage dimensions, audio format, embedded assets).
- Extracted the assets — carved the 12 MP3 samples and 6 bitmap key graphics out as open-format files.
- Wrapped it in Ruffle — an open-source Flash Player emulator compiled to WebAssembly, self-hosted from npm, so the original SWF runs byte-for-byte faithful in any modern browser with no plugin and nothing 'phoning home', as they used to say.
- Rebuilt the page — modernised the old Dreamweaver HTML (stripping the dead MM_ rollover scripts and the <object>/<embed> classid incantation) into clean present-day markup, with a brand new hand-lettered banner replacing the original.
  
Behold, the  
# [XYBERPHON](https://www.displacementactivities.org/xyberphon/)  
...go on, click it!