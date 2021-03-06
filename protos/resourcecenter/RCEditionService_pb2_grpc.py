# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import RCCommon_pb2 as RCCommon__pb2
import RCEditionService_pb2 as RCEditionService__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


class RCEditionServiceStub(object):
  """教材和章节相关的
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.listEditionVersion = channel.unary_unary(
        '/resourcecenter.RCEditionService/listEditionVersion',
        request_serializer=RCEditionService__pb2.RequestEditionVersionList.SerializeToString,
        response_deserializer=RCEditionService__pb2.ResponseEditionVersionList.FromString,
        )
    self.listEdition = channel.unary_unary(
        '/resourcecenter.RCEditionService/listEdition',
        request_serializer=RCEditionService__pb2.RequestEditionList.SerializeToString,
        response_deserializer=RCEditionService__pb2.ResponseEditionList.FromString,
        )
    self.insertEdition = channel.unary_unary(
        '/resourcecenter.RCEditionService/insertEdition',
        request_serializer=RCEditionService__pb2.RequestInsertEdition.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.updateEdition = channel.unary_unary(
        '/resourcecenter.RCEditionService/updateEdition',
        request_serializer=RCEditionService__pb2.RequestUpdateEdition.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.deleteEdition = channel.unary_unary(
        '/resourcecenter.RCEditionService/deleteEdition',
        request_serializer=RCEditionService__pb2.RequestDeleteEdition.SerializeToString,
        response_deserializer=RCEditionService__pb2.BaseResponse.FromString,
        )
    self.listChapter = channel.unary_unary(
        '/resourcecenter.RCEditionService/listChapter',
        request_serializer=RCEditionService__pb2.RequestChapterList.SerializeToString,
        response_deserializer=RCEditionService__pb2.ResponseChapterList.FromString,
        )
    self.listEditionBySubject = channel.unary_unary(
        '/resourcecenter.RCEditionService/listEditionBySubject',
        request_serializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.SerializeToString,
        response_deserializer=RCCommon__pb2.ListResp.FromString,
        )
    self.listGradeByEdition = channel.unary_unary(
        '/resourcecenter.RCEditionService/listGradeByEdition',
        request_serializer=RCEditionService__pb2.SubjectEditionReq.SerializeToString,
        response_deserializer=RCCommon__pb2.ListResp.FromString,
        )
    self.listChapterByEdition = channel.unary_unary(
        '/resourcecenter.RCEditionService/listChapterByEdition',
        request_serializer=RCEditionService__pb2.EditionGradeReq.SerializeToString,
        response_deserializer=RCCommon__pb2.SingleResp.FromString,
        )
    self.listChapterNoPointByEdition = channel.unary_unary(
        '/resourcecenter.RCEditionService/listChapterNoPointByEdition',
        request_serializer=RCEditionService__pb2.EditionGradeReq.SerializeToString,
        response_deserializer=RCCommon__pb2.SingleResp.FromString,
        )


class RCEditionServiceServicer(object):
  """教材和章节相关的
  """

  def listEditionVersion(self, request, context):
    """条件查询教材版本.沪教版,人教版...,
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listEdition(self, request, context):
    """获取教材列表
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def insertEdition(self, request, context):
    """新增教材
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateEdition(self, request, context):
    """修改教材
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteEdition(self, request, context):
    """删除教材
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listChapter(self, request, context):
    """获取某个教材的章节列表
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listEditionBySubject(self, request, context):
    """根据科目查教材版本(结果message EditionVersionVo)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listGradeByEdition(self, request, context):
    """根据科目教材查年级(结果message EditionVo)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listChapterByEdition(self, request, context):
    """根据科目教材年级查章节包含知识点(结果message StringValue)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listChapterNoPointByEdition(self, request, context):
    """根据科目教材年级查章节不包含知识点(结果message StringValue)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RCEditionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'listEditionVersion': grpc.unary_unary_rpc_method_handler(
          servicer.listEditionVersion,
          request_deserializer=RCEditionService__pb2.RequestEditionVersionList.FromString,
          response_serializer=RCEditionService__pb2.ResponseEditionVersionList.SerializeToString,
      ),
      'listEdition': grpc.unary_unary_rpc_method_handler(
          servicer.listEdition,
          request_deserializer=RCEditionService__pb2.RequestEditionList.FromString,
          response_serializer=RCEditionService__pb2.ResponseEditionList.SerializeToString,
      ),
      'insertEdition': grpc.unary_unary_rpc_method_handler(
          servicer.insertEdition,
          request_deserializer=RCEditionService__pb2.RequestInsertEdition.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'updateEdition': grpc.unary_unary_rpc_method_handler(
          servicer.updateEdition,
          request_deserializer=RCEditionService__pb2.RequestUpdateEdition.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'deleteEdition': grpc.unary_unary_rpc_method_handler(
          servicer.deleteEdition,
          request_deserializer=RCEditionService__pb2.RequestDeleteEdition.FromString,
          response_serializer=RCEditionService__pb2.BaseResponse.SerializeToString,
      ),
      'listChapter': grpc.unary_unary_rpc_method_handler(
          servicer.listChapter,
          request_deserializer=RCEditionService__pb2.RequestChapterList.FromString,
          response_serializer=RCEditionService__pb2.ResponseChapterList.SerializeToString,
      ),
      'listEditionBySubject': grpc.unary_unary_rpc_method_handler(
          servicer.listEditionBySubject,
          request_deserializer=google_dot_protobuf_dot_wrappers__pb2.Int32Value.FromString,
          response_serializer=RCCommon__pb2.ListResp.SerializeToString,
      ),
      'listGradeByEdition': grpc.unary_unary_rpc_method_handler(
          servicer.listGradeByEdition,
          request_deserializer=RCEditionService__pb2.SubjectEditionReq.FromString,
          response_serializer=RCCommon__pb2.ListResp.SerializeToString,
      ),
      'listChapterByEdition': grpc.unary_unary_rpc_method_handler(
          servicer.listChapterByEdition,
          request_deserializer=RCEditionService__pb2.EditionGradeReq.FromString,
          response_serializer=RCCommon__pb2.SingleResp.SerializeToString,
      ),
      'listChapterNoPointByEdition': grpc.unary_unary_rpc_method_handler(
          servicer.listChapterNoPointByEdition,
          request_deserializer=RCEditionService__pb2.EditionGradeReq.FromString,
          response_serializer=RCCommon__pb2.SingleResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'resourcecenter.RCEditionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
