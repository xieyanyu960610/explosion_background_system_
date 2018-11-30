# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.sample.serializers import *
from apps.sample.models import *
from utils.permissions import IsAdmin
from bzxt117.settings import MEDIA_ROOT
from utils.PCB import *
from utils.GCMS_handle import *
from apps.evi.models import *
from apps.match.models import *
from apps.match.views import *


    # get方法是请求在url中的参数的，而post是请求在request中的参数的
        # 此时type等都是str类型哦
        # type = int(request.POST["type"])
        # 没法直接用type当成类去做filter
        # result = type.objects.all()
        # python没有switch case
        # if type == 1:
            # 对exploSampleFTIRTestFiles做平均，并回填到exploSampleFTIRTestFile的对应记录的平均后的文件中
            # 如果exploEviFTIR表中的txtHandledURL，即平均过的TXT文档是空的，则直接回填，否则先删去原来的文档再填入。
            # 拿着更新后的文件，去和物证库中的每个物证进行比较，每个得出的分数用get_or_created弄出FTIR表中的记录或者新建
            # FTIR表的记录，记录原来的分数，再更改分数，
            #最后更新维护综合表：拿着物证和样本id去综合表中查，get_or_created，有则根据原来的分数和新的分数进行更新，没有的话就根据新的分数建立记录。
            # 通过exploEvi和exploSample找出综合结果记录，修改Score，同时isCheck和isExpertCheck置为False、checkHandle和expertHandle置为null
                # # exploSyn_Match不能重名exploSynMatch！！
                # exploSyn_Match = exploSynMatch()
                # # 外键空值的时候可以赋值为None,代表数据库中的NULL，且序列化的时候也不会出问题的~
                # exploSyn_Match.checkHandle = None
                # exploSyn_Match.expertHandle_id = 2
       #修改得分，同时核准置为False，核准人员为None
        # 会返回201的response，且因为Response是rest_framework的，因此只能最低使用APIView
class exploSampleViewset(viewsets.ModelViewSet):
    """
    炸药及原材料常见样本管理
    list:
        获取
    create:
        添加
    update:
        更新
    delete:
        删除
    """
    queryset = exploSample.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    serializer_class = exploSampleSerializer
    pagination_class = MyPageNumberPagination
    # IsAuthenticated表示是否登录
    permission_classes = (IsAuthenticated,IsAdmin)

class exploSampleFTIRViewset(viewsets.ModelViewSet):

    queryset = exploSampleFTIR.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = exploSampleFTIRSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return exploSampleFTIRDetailSerializer
        return exploSampleFTIRSerializer
class exploSampleFTIRTestFileViewset(viewsets.ModelViewSet):

    queryset = exploSampleFTIRTestFile.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = LsitExploSampleFTIRTestFileSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    parser_classes = (MultiPartParser, FileUploadParser,)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "create":
            return LsitExploSampleFTIRTestFileSerializer
        return exploSampleFTIRTestFileSerializer

    def perform_destroy(self, instance):
        # 综合表中的对应的值应该更新，减去这个文件对综合匹配结果的影响，同时都置为未匹配
        # 样本库的变化会导致报告表的结果不准确，因此报告表清零
        reports = exploReportMatch.objects.all()
        for report in reports:
            report.delete()
        instance.delete()

class exploSampleRamanViewset(viewsets.ModelViewSet):

    queryset = exploSampleRaman.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = exploSampleRamanSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return exploSampleRamanDetailSerializer
        return exploSampleRamanSerializer
class exploSampleRamanTestFileViewset(viewsets.ModelViewSet):

    queryset = exploSampleRamanTestFile.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = exploSampleRamanTestFileSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    parser_classes = (MultiPartParser, FileUploadParser,)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "create":
            return LsitExploSampleRamanTestFileSerializer
        return exploSampleRamanTestFileSerializer

    def perform_destroy(self, instance):
        # 综合表中的对应的值应该更新，减去这个文件对综合匹配结果的影响，同时都置为未匹配
        # 样本库的变化会导致报告表的结果不准确，因此报告表清零
        reports = exploReportMatch.objects.all()
        for report in reports:
            report.delete()
        instance.delete()

class exploSampleXRDViewset(viewsets.ModelViewSet):

    queryset = exploSampleXRD.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = exploSampleXRDSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return exploSampleXRDDetailSerializer
        return exploSampleXRDSerializer
class exploSampleXRDTestFileViewset(viewsets.ModelViewSet):

    queryset = exploSampleXRDTestFile.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class =exploSampleXRDTestFileSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    parser_classes = (MultiPartParser, FileUploadParser,)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "create":
            return LsitExploSampleXRDTestFileSerializer
        return exploSampleXRDTestFileSerializer

    def perform_destroy(self, instance):
        # 综合表中的对应的值应该更新，减去这个文件对综合匹配结果的影响，同时都置为未匹配
        # 样本库的变化会导致报告表的结果不准确，因此报告表清零
        reports = exploReportMatch.objects.all()
        for report in reports:
            report.delete()
        instance.delete()

class exploSampleXRFViewset(viewsets.ModelViewSet):

    queryset = exploSampleXRF.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = exploSampleXRFSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return exploSampleXRFDetailSerializer
        return exploSampleXRFSerializer
class exploSampleXRFTestFileViewset(viewsets.ModelViewSet):

    queryset = exploSampleXRFTestFile.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = exploSampleXRFTestFileSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    parser_classes = (MultiPartParser, FileUploadParser,)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "create":
            return LsitExploSampleXRFTestFileSerializer
        return exploSampleXRFTestFileSerializer

    def perform_destroy(self, instance):
        # 综合表中的对应的值应该更新，减去这个文件对综合匹配结果的影响，同时都置为未匹配
        # 样本库的变化会导致报告表的结果不准确，因此报告表清零
        reports = exploReportMatch.objects.all()
        for report in reports:
            report.delete()
        instance.delete()

class exploSampleGCMSViewset(viewsets.ModelViewSet):

    queryset = exploSampleGCMS.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = exploSampleGCMSSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return exploSampleGCMSDetailSerializer
        return exploSampleGCMSSerializer
class exploSampleGCMSTestFileViewset(viewsets.ModelViewSet):

    queryset = exploSampleGCMSTestFile.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = exploSampleGCMSTestFileSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    parser_classes = (MultiPartParser, FileUploadParser,)

    def get_serializer_class(self):
        if self.action == "create":
            return LsitExploSampleGCMSTestFileSerializer
        return exploSampleGCMSTestFileSerializer

    def perform_destroy(self, instance):
        # 综合表中的对应的值应该更新，减去这个文件对综合匹配结果的影响，同时都置为未匹配
        # 样本库的变化会导致报告表的结果不准确，因此报告表清零
        reports = exploReportMatch.objects.all()
        for report in reports:
            report.delete()
        instance.delete()

class devSampleViewset(viewsets.ModelViewSet):
    queryset = devSample.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    serializer_class = devSampleSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    pagination_class = MyPageNumberPagination
class devPartSampleViewset(viewsets.ModelViewSet):
    queryset = devPartSample.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    serializer_class = devPartSampleSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    pagination_class = MyPageNumberPagination

class devPartSampleFTIRViewset(viewsets.ModelViewSet):
    queryset = devPartSampleFTIR.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = devPartSampleFTIRSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return devPartSampleFTIRDetailSerializer
        return devPartSampleFTIRSerializer
class devPartSampleFTIRTestFileViewset(viewsets.ModelViewSet):
    queryset = devPartSampleFTIRTestFile.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = devPartSampleFTIRTestFileSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    parser_classes = (MultiPartParser, FileUploadParser,)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "create":
            return LsitdevPartSampleFTIRTestFileSerializer
        return devPartSampleFTIRTestFileSerializer

    def perform_destroy(self, instance):
        # 综合表中的对应的值应该更新，减去这个文件对综合匹配结果的影响，同时都置为未匹配
        # 样本库的变化会导致报告表的结果不准确，因此报告表清零
        synMatchs = devSynMatch.objects.objects.all()
        for synMatch in synMatchs:
            synMatch.delete()
        instance.delete()

class devPartSampleRamanViewset(viewsets.ModelViewSet):
    queryset = devPartSampleRaman.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = devPartSampleRamanSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return devPartSampleRamanDetailSerializer
        return devPartSampleRamanSerializer
class devPartRamanTestFileViewset(viewsets.ModelViewSet):
    queryset = devPartRamanTestFile.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = devPartRamanTestFileSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    parser_classes = (MultiPartParser, FileUploadParser,)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "create":
            return LsitdevPartSampleRamanTestFileSerializer
        return devPartSampleRamanTestFileSerializer

    def perform_destroy(self, instance):
        # 综合表中的对应的值应该更新，减去这个文件对综合匹配结果的影响，同时都置为未匹配
        # 样本库的变化会导致报告表的结果不准确，因此报告表清零
        synMatchs = devSynMatch.objects.objects.all()
        for synMatch in synMatchs:
            synMatch.delete()
        instance.delete()

class devPartSampleXRFViewset(viewsets.ModelViewSet):
    queryset = devPartSampleXRF.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = devPartSampleXRFSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return devPartSampleXRFDetailSerializer
        return devPartSampleXRFSerializer
class devPartSampleXRFTestFileViewset(viewsets.ModelViewSet):
    queryset = devPartSampleXRFTestFile.objects.all()
    #queryset = exploSample.objects.filter(sname="样本3")
    # serializer_class = devPartSampleXRFTestFileSerializer
    permission_classes = (IsAuthenticated,IsAdmin)
    parser_classes = (MultiPartParser, FileUploadParser,)
    pagination_class = MyPageNumberPagination
    def get_serializer_class(self):
        if self.action == "create":
            return LsitdevPartSampleXRFTestFileSerializer
        return devPartSampleXRFTestFileSerializer

    def perform_destroy(self, instance):
        # 综合表中的对应的值应该更新，减去这个文件对综合匹配结果的影响，同时都置为未匹配
        # 样本库的变化会导致报告表的结果不准确，因此报告表清零
        synMatchs = devSynMatch.objects.objects.all()
        for synMatch in synMatchs:
            synMatch.delete()
        instance.delete()

class devShapeSampleViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,IsAdmin)
    queryset = devShapeSample.objects.all()
    serializer_class = devShapeSampleSerializer
    pagination_class = MyPageNumberPagination
    # 使用方法：create即新建的时候只上传图片，矩形坐标之类的都是在更新的接口做的，而且是部分更新接口（用docs），第一次更新写入矩形框坐标，在样本点.txt中，
    # 第二次更新什么都不用填
    def perform_create(self, serializer):
        sample = serializer.save()
        id = sample.id
        #重命名
        name = str(sample.originalUrl).split("/")[-1]
        picType = os.path.splitext(name)[1]
        path = os.path.join(MEDIA_ROOT,"image/devShapeSample/original/")
        os.rename(os.path.join(MEDIA_ROOT,str(sample.originalUrl)), os.path.join(path, str(id) + picType))
        sample.originalUrl = "image/devShapeSample/original/" + str(id) + picType
        sample.save()
        return sample


    def perform_update(self, serializer):
        sample = serializer.save()
        id =sample.id
        middle = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "utils/middle/")
        if sample.isFirst == True:
            middle = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "utils/middle/")

            # 写文件
            rectUrl = os.path.join(middle, str(id) + "-1.txt")
            proUrl = os.path.join(middle, str(id) + "-2.txt")
            backUrl = os.path.join(middle, str(id) + "-3.txt")
            boardUrl = os.path.join(middle, str(id) + "-4.txt")

            rect = open(rectUrl, "w")
            rect.write(sample.rectCoordi)
            rect.close()
            pro = open(proUrl, "w")
            pro.write(sample.proCoordi)
            pro.close()
            back = open(backUrl, "w")
            back.write(sample.backCoordi)
            back.close()
            board = open(boardUrl, "w")
            board.write(sample.boardCoordi)
            board.close()

            getPCB(id, "Sample")

            sample.blackWhiteUrl = "image/devShapeSample/blackWhite/" + str(id) + ".jpg"
            sample.interColorUrl = "image/devShapeSample/interColor/" + str(id) + ".jpg"
            sample.middleResultUrl = "file/devShapeSample/middleResult/" + str(id) + ".txt"

            os.remove(rectUrl)
            os.remove(proUrl)
            os.remove(backUrl)
            os.remove(boardUrl)

            sample.save()
        else:
            compCheckUrl = os.path.join(middle,str(id) + "-5.txt")
            boardCheckUrl = os.path.join(middle,str(id) + "-6.txt")

            compCheck = open(compCheckUrl,"w")
            compCheck.write(sample.compCheckCoordi)
            compCheck.close()
            boardCheck = open(boardCheckUrl,"w")
            boardCheck.write(sample.boardCheckCoordi)
            boardCheck.close()

            segComp(id, "Sample")

            sample.featureUrl = "file/devShapeSample/feature/"+str(id)+".harris"
            sample.resultPicUrl = "image/devShapeSample/result/"+str(id)+".jpg"
            sample.resultFileUrl = "file/devShapeSample/result/"+str(id)+".seg"

            os.remove(compCheckUrl)
            os.remove(boardCheckUrl)

            sample.save()
        return sample

    def perform_destroy(self, instance):
        # originalUrl= os.path.join(MEDIA_ROOT,str( instance.originalUrl))
        # if os.path.exists(originalUrl):
        #     os.remove(originalUrl)
        instance.delete()
