# 마이 페이지와 나의 거래내역 확인 기능 담당
from flask import Blueprint, render_template, redirect, url_for, flash, request

per = Blueprint('personal', __name__, url_prefix='/')


@per.route('/my-page')
def my_page():
    return render_template('mypage.html')
