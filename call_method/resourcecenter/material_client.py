#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/4/16 10:41
"""
import grpc
import yaml
import os
from google.protobuf import wrappers_pb2
from protos.resourcecenter import RCMaterialService_pb2, RCMaterialService_pb2_grpc
from google.protobuf.json_format import MessageToDict

BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path= BASE_DIR+ '/datas/env.yml'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = yaml.safe_load(file)
    # print(datas)

class Material(object):
    def __init__(self):
        self.base_url = datas['HOST'] + ':' + datas['PORT']
        self.conn = grpc.insecure_channel(self.base_url)
        self.client = RCMaterialService_pb2_grpc.RCMaterialServiceStub(channel=self.conn)

    # 新建素材
    def createMaterial(self, id, name, teacherId, createType, url, size, categoryId, customerId, subjectId, chapterId,
                       pointId, fascicle, editionId):
        response = self.client.createMaterial(RCMaterialService_pb2.ModifyMaterial
                                              (id= id, name= name, teacherId= teacherId, createType= createType,
                                               url= url, size= size, categoryId= categoryId, customerId= customerId,
                                               subjectId= subjectId, chapterId= chapterId, pointId= pointId,
                                               fascicle= fascicle, editionId= editionId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 查询素材
    def listMaterial(self, name, teacherId, createType, categoryId, customerId, subjectId,chapterId, pointId, gradeId,editionId,materialUsageStatistic,
                     updateTimeStatistic, searchContent, isBoutique, pageNo, pageSize):
        response = self.client.listMaterial(RCMaterialService_pb2.ListMaterialsRequest
                                           (name= name, teacherId= teacherId, createType= createType,
                                            categoryId= categoryId, customerId= customerId, subjectId= subjectId,
                                            chapterId= chapterId, pointId= pointId,gradeId= gradeId,editionId=editionId,
                                            materialUsageStatistic= materialUsageStatistic,
                                            updateTimeStatistic= updateTimeStatistic, searchContent= searchContent,
                                            isBoutique= isBoutique, pageNo= pageNo, pageSize= pageSize))
        res = MessageToDict(response)
        # print(res)
        return res

    # 根据类别查询素材
    def listMaterialByCategory(self, subjectId, customerId, searchContent, categoryIds, isBoutique):
        response = self.client.listMaterialByCategory(RCMaterialService_pb2.GetMaterialByCategoryRequest
                                           (subjectId= subjectId, customerId= customerId, searchContent= searchContent,
                                            categoryIds= categoryIds, isBoutique= isBoutique))
        res = MessageToDict(response)
        # print(res)
        return res

    # 根据id查询素材
    def getMaterialById(self, id, subjectId, customerId):
        response = self.client.getMaterialById(RCMaterialService_pb2.GetMaterialByIdRequest
                                           (id= id, subjectId= subjectId, customerId= customerId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 根据包查询素材
    def listMaterialByPackage(self, id, subjectId, customerId):
        response = self.client.listMaterialByPackage(RCMaterialService_pb2.GetMaterialByPackageRequest
                                           (id= id, subjectId= subjectId, customerId= customerId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 修改素材
    def updateMaterial(self, id, name, teacherId, createType, categoryId, customerId, subjectId, chapterId,
                       pointId, fascicle, editionId):
        response = self.client.updateMaterial(RCMaterialService_pb2.ModifyMaterial
                                              (id= id, name= name, teacherId= teacherId, createType= createType,
                                               categoryId= categoryId, customerId= customerId, subjectId= subjectId,
                                               chapterId= chapterId, pointId= pointId,fascicle= fascicle,
                                               editionId= editionId))
        res = MessageToDict(response)
        # print(res)
        return res

    # 修改素材精品
    def updateBoutiqueMaterial(self, id, isBoutique, subjectId, customerId):
        response = self.client.updateBoutiqueMaterial(RCMaterialService_pb2.UpdateMaterialBoutiqueRequest
                                                      (id= id, isBoutique= isBoutique, subjectId= subjectId,
                                                       customerId= customerId))
        res = MessageToDict(response)
        # print(res)
        return res

    #查询素材类别
    def listCategory(self):
        response = self.client.listCategory(RCMaterialService_pb2.listMaterialRequest())

        res = MessageToDict(response)
        # print(res)
        return res

if __name__ == '__main__':
    M= Material()
    result= M.createMaterial(id= None, name= '图片啊啊啊啊',teacherId= None, createType= 2,
                             url= 'http://szwd.oss-cn-qingdao.aliyuncs.com/files/3d8b96669a534afcb825a94f816adefb.jpg',
                             size= 23230, categoryId=6, customerId= None, subjectId= 117, chapterId= 26878,
                             pointId= None, fascicle= 1, editionId= None)
    # result= M.listMaterial(name= None, teacherId= None,  createType= None, categoryId= None, customerId= None,
    #                        subjectId= 102, chapterId= None, pointId= None, gradeId=None,editionId=None,
    #                        materialUsageStatistic= None,updateTimeStatistic= 2, searchContent= '除数', isBoutique= None,
    #                        pageNo= 1, pageSize= 10)
    # result= M.listMaterialByCategory(subjectId= 102, customerId= None, searchContent= None, categoryIds= [4,3],
    #                                  isBoutique= None)
    # result= M.getMaterialById(id= '4dfdf64e-a726-46f0-8e12-e8846afe6ee2', subjectId= 102, customerId= 9102000000)
    # result= M.listMaterialByPackage(id= '1365ed10-6b33-4ad7-a135-fb8e630d8eec', subjectId= 102, customerId= 9102000000)
    # result= M.updateMaterial(id= '7d402c98-cc91-46f1-b2a9-1970b39d5f3e', name= '测试数据-改.ppt', teacherId= None,
    #                          createType= 1,  categoryId= 4, customerId= None, subjectId= 102, chapterId= None,
    #                          pointId= [2458], fascicle= None, editionId= None)
    # result= M.updateBoutiqueMaterial(id= '7dffda1f-5ab5-42a7-a577-e44a87a46862', isBoutique= 1, subjectId= 102,
    #                                  customerId= 4403051000)
    # result= M.listCategory()

    print(result)