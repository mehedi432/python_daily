# আজকে আমরা দেখার চেষ্টা করবো আমরা কীভাবে পাইথন ব্যাবহার করে একটা sqlite3 ডাটাবেইস তৈরি করতে পারি ।


### আমরা এর জন্যে একটা Library ব্যাবহার করবো যেটা আমাদেরকে সাহায্য করবে একটি json ফাইল থেকে sqlite3 ডাটাবেইস এ কনভার্ট করার জন্যে ।

এই কাজের ধাপ গুলো নিচে দেওয়া হল :
```sh
  # প্রথমেই আমাদের দেখতে হবে পাইথন আমদের সিস্টেমে আছে কিনা 
  python --version
  
  # তারপর আমাদের virtual environment বলে দিতে হবে ।
  python3 -m venv venv

  # এখন আমাদের এই virtual environment কে activate করে দিতে হবে
  source venv/bin/activate

  # আমাদেরকে এখন একটা package install করতে হবে। 
  pip3 install sqlitebiter

  # এখন আমরা এই package ব্যাবহার করতে হবে এর জন্যে আমাদের প্রয়োজন আমরা যেই json ফাইলকে কনভার্ট করবো সেই folder এ যাওয়া লাগবে অথবা সেই folder এ থাকা লাগবে। তারপর আমাদের একটা কমান্ড লিখা লাগবে, এই কমান্ড এর আউটপুট হিসাবে সকল কিছুকে sample.sqlite নামে save হবে 
  sqlitebiter -o sample.sqlite file *

  # এখন আমরা যদি চাই আমরা আমাদের কেবল একটা ফাইল কে কনভার্ট করবো তাহলে আমাদের ফাইল এর নাম বলে দিতে হবে
  sqlitebiter -o sample.sqlite file ayats_bn.json

  # আমরা ইচ্ছা করলে আমাদের ফাইল এর extension পরিবর্তন করতে পারি, সেটার জন্যে আমাদেরকে উপরের কমান্ড এর সামান্য পরিবর্তন করতে হবে
  sqlitebiter -o sample.db file ayats_bn.json

```
