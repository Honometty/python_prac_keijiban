from django.shortcuts import render
from flask import Flask, session, redirect

USERLIST = {
  'taro': 'aaa', 
  'jiro': 'bbb', 
  'sabu': 'ccc'
}

# ログインして調べる
def is_login():
  return 'login' in session

# ログイン処理
def try_login(user, password):
  if user not in USERLIST:
    return False
  if USERLIST[user] != password:
    return False
  session['login'] = user
  return True

# ログアウト処理
def try_logout():
  session.pop('login', None)
  return True

# セッションからユーザ名を得る
def get_user():
  if is_login():
    return session['login']
  return False