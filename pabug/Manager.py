# encoding:utf-8
from tokenize import String


class User:
    def __init__(self):
        print()
    def __del__(self):
        print()
    def userPrint(self):
        print(self)
    #定义基本属性

    mode: String

    token: String

    latitude: String

    longitude: String

    user_id: String

    sex: String

    user_name: String

    nick_name: String

    mobile: String

    is_bind_mobile: String

    email: String

    is_bind_email: String

    signature: String

    set_face_time: String

    roles: String

    reg_zone: String

    reg_source: String

    is_agree_clause: String

    pub_id: String

    tech_status: String
    country: String

    province: String
    city: String

    district: String

    street: String

    nation_id: String

    face_url: String

    config: String
    zipcode: String

    repairCode: String

    repairName: String

    technician_address: String


    produceID = 0
    serialNoList: []

    serialnoType: String

    account: String

    password: String

