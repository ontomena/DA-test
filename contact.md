---
layout: default
title: contact
permalink: /contact/
---

<div id="contact-page">
<div class="home-content">

<p>DisplacementActivities is the site according to Simon Bradley, combining archives with new material. I work with sound mainly, one way or another: oral history, installation, performance, locative media. I like to find ways to bring sound to experience, often from apparent silence—and vice versa.</p>

<p>Please use form below if you'd like to get in touch:</p>

<style>
.contact-form {
  margin: 1.5em 0 2em;
}
.contact-form label {
  display: block;
  font-size: 0.85em;
  margin-top: 1.2em;
  margin-bottom: 0.3em;
  letter-spacing: 0.03em;
}
.contact-form input[type="text"],
.contact-form input[type="email"],
.contact-form textarea {
  width: 100%;
  max-width: 480px;
  border: none;
  border-bottom: 1px solid currentColor;
  padding: 0.3em 0;
  font-family: inherit;
  font-size: 1em;
  background: transparent;
  box-sizing: border-box;
  outline: none;
  border-radius: 0;
  -webkit-appearance: none;
}
.contact-form textarea {
  height: 110px;
  resize: vertical;
  border: 1px solid currentColor;
  padding: 0.4em 0.5em;
  display: block;
}
.contact-form button {
  display: inline-block;
  margin-top: 1.2em;
  background: none;
  border: none;
  font-family: inherit;
  font-size: 0.9em;
  cursor: pointer;
  padding: 0;
  text-decoration: underline;
  text-underline-offset: 3px;
}
.contact-form button:hover {
  opacity: 0.55;
}
</style>

<form class="contact-form" action="https://formspree.io/f/mbdekjwo" method="POST">
  <label for="cf-name">name</label>
  <input type="text" id="cf-name" name="name" required>
  <label for="cf-email">email</label>
  <input type="email" id="cf-email" name="email" required>
  <label for="cf-message">message</label>
  <textarea id="cf-message" name="message" required></textarea>
  <button type="submit">send</button>
</form>

<hr style="margin: 30px 0; border: none; border-top: 1px solid #e0e0e0;">

<h2 style="font-size: 1.1em; font-weight: normal; margin-bottom: 15px;">subscribe</h2>

<form
  action="https://buttondown.email/api/emails/embed-subscribe/ontomena"
  method="post"
  target="popupwindow"
  onsubmit="window.open('https://buttondown.email/ontomena', 'popupwindow')"
  style="margin-bottom: 10px;"
>
  <input type="email" name="email" placeholder="your@email.com" required style="padding: 5px 0; width: 240px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 0.95em; border: none; border-bottom: 1px solid currentColor; outline: none; background: transparent;" />
  <input type="submit" value="subscribe →" style="background: none; border: none; padding: 0 0 0 10px; font-family: inherit; font-size: 0.9em; cursor: pointer; text-decoration: underline; text-underline-offset: 3px;" />
</form>

<hr style="margin: 30px 0; border: none; border-top: 1px solid #e0e0e0;">

<p><a href="{{ '/feed.xml' | relative_url }}" style="font-size: 0.95em; color: inherit; text-decoration: underline; text-underline-offset: 3px;">RSS feed →</a></p>

<hr style="margin: 30px 0; border: none; border-top: 1px solid #e0e0e0;">

<p style="font-size: 0.9em; color: #666;">This site was put together on Github using GitHub Desktop and Visual Studio Code, all freely available.</p>

</div>
</div>
