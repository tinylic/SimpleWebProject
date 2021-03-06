# -*- coding: UTF-8 -*-
"""
社区管理页面的一些操作
"""
import json
from flask import render_template, session, request
from webapp import app
from db.db_community import *
__author__ = 'sonnyhcl'


@app.route('/community', methods=['GET'])
def community_index():
    return render_template('views/community.html', role='root')


@app.route('/community/<int:c_id>', methods=['POST'])
def get_community(c_id):
    status, info = community.get_community(c_id)
    ret = {"data": [], "status": status, "msg":""}
    if status == "Success":
        _ = [ret['data'].append({'c_id':i[0],
                                 'c_name':i[1]}) for i in info]
    else:
        ret['msg'] = info
    return json.dumps(ret, ensure_ascii=False)


@app.route('/community/page/', methods=['POST'])
def show_communities():
    """
    :param :
    :return:
    """
    cid = session['c_id']
    status, info = community.get_community(cid)
    ret = {"data": [], "status": status, "msg": ""}
    if status == "Success":
        _ = [ret['data'].append({'c_id': i[0],
                                 'c_name': i[1]}) for i in info]
    else:
        ret['msg'] = info
    return json.dumps(ret, ensure_ascii=False)


@app.route('/community/add', methods=['POST'])
def add_community():
    c_name = request.form.get('c_name')
    status = community.add_community(c_name)
    return status


@app.route('/community/modify', methods=['POST'])
def modify_community():
    c_name = request.form.get('c_name')
    c_id = request.form.get('c_id')
    status = community.update_community(c_id=c_id, new_c_name=c_name)
    return status


@app.route('/community/delete', methods=['POST'])
def delete_community():
    c_id = request.form.get('c_id')
    status = community.delete_community(c_id)
    return status


