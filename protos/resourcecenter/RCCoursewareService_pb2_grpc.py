# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import RCCommon_pb2 as RCCommon__pb2
import RCCoursewareService_pb2 as RCCoursewareService__pb2


class RCCoursewareServiceStub(object):
  """课件相关的
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.insertCourseware = channel.unary_unary(
        '/resourcecenter.RCCoursewareService/insertCourseware',
        request_serializer=RCCoursewareService__pb2.ReqInsertCourseware.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.isJingCourseware = channel.unary_unary(
        '/resourcecenter.RCCoursewareService/isJingCourseware',
        request_serializer=RCCoursewareService__pb2.ReqCoursewareIsJing.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.insertCoursewarePage = channel.unary_unary(
        '/resourcecenter.RCCoursewareService/insertCoursewarePage',
        request_serializer=RCCoursewareService__pb2.CoursewarePageVo.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.updateCoursewarePage = channel.unary_unary(
        '/resourcecenter.RCCoursewareService/updateCoursewarePage',
        request_serializer=RCCoursewareService__pb2.CoursewarePageVo.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.deleteCoursewarePage = channel.unary_unary(
        '/resourcecenter.RCCoursewareService/deleteCoursewarePage',
        request_serializer=RCCoursewareService__pb2.CoursewarePageVo.SerializeToString,
        response_deserializer=RCCommon__pb2.EmptyResp.FromString,
        )
    self.listCourseware = channel.unary_unary(
        '/resourcecenter.RCCoursewareService/listCourseware',
        request_serializer=RCCoursewareService__pb2.ReqCoursewareList.SerializeToString,
        response_deserializer=RCCoursewareService__pb2.ResponseCoursewareList.FromString,
        )


class RCCoursewareServiceServicer(object):
  """课件相关的
  """

  def insertCourseware(self, request, context):
    """新增课件
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def isJingCourseware(self, request, context):
    """课件加精/取消加精
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def insertCoursewarePage(self, request, context):
    """新增课件的页
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateCoursewarePage(self, request, context):
    """修改课件的页
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteCoursewarePage(self, request, context):
    """删除课件的页.只传coursewareId,pageNum字段
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def listCourseware(self, request, context):
    """条件查询课件列表
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RCCoursewareServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'insertCourseware': grpc.unary_unary_rpc_method_handler(
          servicer.insertCourseware,
          request_deserializer=RCCoursewareService__pb2.ReqInsertCourseware.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'isJingCourseware': grpc.unary_unary_rpc_method_handler(
          servicer.isJingCourseware,
          request_deserializer=RCCoursewareService__pb2.ReqCoursewareIsJing.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'insertCoursewarePage': grpc.unary_unary_rpc_method_handler(
          servicer.insertCoursewarePage,
          request_deserializer=RCCoursewareService__pb2.CoursewarePageVo.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'updateCoursewarePage': grpc.unary_unary_rpc_method_handler(
          servicer.updateCoursewarePage,
          request_deserializer=RCCoursewareService__pb2.CoursewarePageVo.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'deleteCoursewarePage': grpc.unary_unary_rpc_method_handler(
          servicer.deleteCoursewarePage,
          request_deserializer=RCCoursewareService__pb2.CoursewarePageVo.FromString,
          response_serializer=RCCommon__pb2.EmptyResp.SerializeToString,
      ),
      'listCourseware': grpc.unary_unary_rpc_method_handler(
          servicer.listCourseware,
          request_deserializer=RCCoursewareService__pb2.ReqCoursewareList.FromString,
          response_serializer=RCCoursewareService__pb2.ResponseCoursewareList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'resourcecenter.RCCoursewareService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
