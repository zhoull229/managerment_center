#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/28 17:27
"""
import grpc
import yaml
import os
from protos.resourcecenter import RCReviewService_pb2,RCReviewService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class Review(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCReviewService_pb2_grpc.RCReviewServiceStub(channel=self.conn)

    # 提交审核
    def submitResource(self, id, resourceType, subjectId, customerId):
        response = self.client.submitResource(RCReviewService_pb2.Resource2ReviewReq
                                              (id= id, resourceType= resourceType, subjectId= subjectId,
                                               customerId= customerId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 审核资源
    def reviewResource(self, id, resourceType, subjectId, customerId, userId, remark, reviewStatus):
        response = self.client.reviewResource(RCReviewService_pb2.ReviewResourceReq
                                              (id= id, resourceType= resourceType, subjectId= subjectId,
                                               customerId= customerId, userId= userId, remark= remark,
                                               reviewStatus= reviewStatus))
        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    R= Review()
    # result = R.submitResource(id= '1', resourceType= 2, subjectId= 3, customerId= 4403051000)
    result = R.reviewResource(id= 'fea58334-77e0-4049-b80f-18aacaf68a08', resourceType= 10, subjectId= 101,
                              customerId= None, userId= 'cc8becda-667c-11e9-bc0d-525400a29c3d', remark= '6', reviewStatus= 1)
    print(result)