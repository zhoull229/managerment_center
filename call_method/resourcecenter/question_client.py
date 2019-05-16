#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/12 10:51
"""
import grpc
import yaml
import os
import json
from protos.resourcecenter import RCQuestionService_pb2, RCQuestionService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class Question(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCQuestionService_pb2_grpc.RCQuestionServiceStub(channel=self.conn)

    # 新建试题
    def createQuestion(self, id, subjectId, style, difficulty, parentId, seq, labelType, pointId, abilityId,
                       conceptTypeId, conceptTarget, creatorId, customerId, originalCustomerId, gradeId, chapterId,
                       createType, refQuestionId, body, answer, selection, errorType, errorAnalysis):
        response = self.client.createQuestion(RCQuestionService_pb2.QuestionReq
                                              (id= id, subjectId= subjectId, style= style, difficulty= difficulty,
                                               parentId= parentId, seq= seq, labelType= labelType, pointId= pointId,
                                               abilityId= abilityId, conceptTypeId= conceptTypeId,
                                               conceptTarget= conceptTarget, creatorId= creatorId,
                                               customerId= customerId, originalCustomerId= originalCustomerId,
                                               gradeId= gradeId, chapterId= chapterId, createType= createType,
                                               refQuestionId= refQuestionId, body= body, answer= answer,
                                               selection= selection, errorType= errorType,errorAnalysis= errorAnalysis))
        res = MessageToDict(response)
        # print(res)
        return res

    # 修改试题
    def updateQuestion(self, id, subjectId, style, difficulty, parentId, seq, labelType, pointId, abilityId,
                       conceptTypeId, conceptTarget, creatorId, customerId, originalCustomerId, gradeId, chapterId,
                       createType, refQuestionId, body, answer, selection, errorType, errorAnalysis):
        response = self.client.updateQuestion(RCQuestionService_pb2.QuestionReq
                                              (id= id, subjectId= subjectId, style= style, difficulty= difficulty,
                                               parentId= parentId, seq= seq, labelType= labelType, pointId= pointId,
                                               abilityId= abilityId, conceptTypeId= conceptTypeId,
                                               conceptTarget= conceptTarget, creatorId= creatorId,
                                               customerId= customerId, originalCustomerId= originalCustomerId,
                                               gradeId= gradeId, chapterId= chapterId, createType= createType,
                                               refQuestionId= refQuestionId, body= body, answer= answer,
                                               selection= selection, errorType= errorType,errorAnalysis= errorAnalysis))
        res = MessageToDict(response)
        # print(res)
        return res

    # 删除试题
    def deleteQuestion(self, id, subjectId):
        response = self.client.deleteQuestion(RCQuestionService_pb2.SingleQuestionReq
                                              (id =id, subjectId= subjectId))

        res = MessageToDict(response)
        # print(res)
        return res

    # 根据id查询试题
    def querySingleQuestion(self, id):
        response = self.client.querySingleQuestion(RCQuestionService_pb2.SingleQuestionReq
                                                   (id =id))

        res = MessageToDict(response)
        # print(res)
        return res

    # 分页查询
    def queryPageQuestion(self, pageNo, pageSize, subjectId, customerId, labelType, gradeId, chapterId, pointId, style,
                          abilityId, conceptTypeId, questionCategory, hardDegreeId, sourceId, timeOrder):
        response = self.client.queryPageQuestion(RCQuestionService_pb2.PageQuestionReq
                                                   (pageNo= pageNo, pageSize= pageSize, subjectId= subjectId,
                                                    customerId= customerId, labelType= labelType, gradeId= gradeId,
                                                    chapterId= chapterId, pointId= pointId, style= style,
                                                    abilityId= abilityId, conceptTypeId= conceptTypeId,
                                                    questionCategory= questionCategory, hardDegreeId= hardDegreeId,
                                                    sourceId= sourceId, timeOrder= timeOrder))
        res = MessageToDict(response)
        # print(res)
        return res

    # 查询待审核/审核通过/不通过列表
    def queryReviewQuestion(self, pageNo, pageSize, reviewStatus, userId, editionVersionId, gradeId, fascicleId,
                            subjectId):
        response = self.client.queryReviewQuestion(RCQuestionService_pb2.ReviewQuestionPageReq
                                                   (pageNo= pageNo, pageSize= pageSize, reviewStatus= reviewStatus,
                                                    userId= userId, editionVersionId= editionVersionId,
                                                    gradeId= gradeId, fascicleId= fascicleId,subjectId= subjectId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 查询我建的题/我的分享
    def queryMyQuestion(self, pageNo, pageSize, subjectId, customerId, reviewStatus, creatorId, labelType,
                        startDate, endDate,):
        response = self.client.queryMyQuestion(RCQuestionService_pb2.MyQuestionReq
                                                   (pageNo= pageNo, pageSize= pageSize, subjectId= subjectId,
                                                    customerId= customerId,reviewStatus= reviewStatus,
                                                    creatorId= creatorId, labelType= labelType,
                                                    startDate= startDate, endDate= endDate))
        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    Q = Question()
    # result = Q.createQuestion(id= None, subjectId= 102, style= 1, difficulty= 4, parentId= None, seq= None, labelType= 1,
    #                           pointId= None, abilityId= ['1', '2'], conceptTypeId= ['1', '2'], conceptTarget= '教学目标',
    #                           creatorId= '73754b91303d11e9a6cc525400a29c3d', customerId= None,
    #                           originalCustomerId= None, gradeId= 13, chapterId= [1449], createType= 2, refQuestionId= None,
    #                           body= '题干xxsssxxddx', answer= json.dumps(['0','1']),
    #                           selection= json.dumps(['选项1','选项2', '选项3','选项4']),
    #                           errorType= json.dumps(['错误1','', '错误3','错误4']),
    #                           errorAnalysis= json.dumps(['原因1','', '原因3','原因14']))
    # result = Q.updateQuestion(id= '7d402c98-cc91-46f1-b2a9-1970b39d5f3e', subjectId= 101, style= 3, difficulty= 4,
    #                           parentId= '父亲', seq= 119, labelType= 1, pointId= [8, 9], abilityId= ['1'],
    #                           conceptTypeId= ['2'],conceptTarget= '教学目标', creatorId= '12', customerId= None,
    #                           originalCustomerId= 0, gradeId= 15, chapterId= [16], createType= 1, refQuestionId= '18',
    #                           body= '19', answer= '20', selection= '21', errorType= '错误类型', errorAnalysis= '错误原因')
    # result= Q.deleteQuestion(id= '02291768-37cd-42b7-9895-7fb43032b1a9',subjectId=209)
    # result= Q.querySingleQuestion(id= '02291768-37cd-42b7-9895-7fb43032b1a9')
    result= Q.queryPageQuestion(pageNo= 1, pageSize= 10, subjectId= 209, customerId= 9209000000, labelType= 2,
                                gradeId= None, chapterId= 4580, pointId= None, style= None, abilityId= None,
                                conceptTypeId= None,questionCategory= None, hardDegreeId= None, sourceId= None,
                                timeOrder= 2)
    # result= Q.queryReviewQuestion(pageNo= 1, pageSize= 10, reviewStatus= 3, userId= None, editionVersionId= None,
    #                               gradeId= None, fascicleId= None,subjectId= 101)
    # result= Q.queryMyQuestion(pageNo= 1, pageSize= 10, subjectId= 101, customerId= None, reviewStatus= 1,
    #                           creatorId= '73754b91303d11e9a6cc525400a29c3d', labelType= 1, startDate= '2019-04-29',
    #                           endDate= '2019-05-30')
    print(result)