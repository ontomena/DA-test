---
layout: post
title: "xyberphon resurrection"
date: 2026-06-06
categories: [sound]
tags: [projects, research]
image: /assets/images/xyberphon-thumb.jpg
excerpt: "A tuneful resurrection from the past web archives"
---
In the misty days of 1999, or thereabouts, I used to spend a lot of time messing about with tools like Dreamweaver and Flash---a great pairing for creating loads of outlandish web elements back in the day. 

One of the things I came up with that seemed to go down pretty well was the xyberphon. It was a simple instrument drawn from samples I made of an Indonesian metallophone (saron) that Phil Moody gave me one birthday. 

The .swf files output by Flash gradually lost support and finally died in 2020 taking with them the whole Macromedia communit that had grown around them. But... now it is possible to bring these things back! Here's how I did it--with a little bit of help from Claude ;-)

- Unpacked the SWF — parsed the binary format directly to inventory exactly what was inside the original (tag types, stage dimensions, audio format, embedded assets).
- Extracted the assets — carved the 12 MP3 samples and 6 bitmap key graphics out as open-format files.
- Wrapped it in Ruffle — an open-source Flash Player emulator compiled to WebAssembly, self-hosted from npm, so the original SWF runs byte-for-byte faithful in any modern browser with no plugin and nothing 'phoning home', as they used to say.
- Rebuilt the page — modernised the old Dreamweaver HTML (stripping the dead MM_ rollover scripts and the <object>/<embed> classid incantation) into clean present-day markup, with a brand new hand-lettered banner replacing the original.
<div style="margin-top: 2rem;">
<p style="margin-bottom: 0;">Behold, the</p>
<h1 style="margin-top: 0 !important; margin-bottom: 0 !important;"><a href="https://www.displacementactivities.org/xyberphon/">XYBERPHON</a></h1>
<p style="margin-top: 0;">...go on, click it!</p>
</div>