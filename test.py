# class AnonymousSurvey():
#     '''
#     收集匿名调查问卷的答案
#     '''
#
#     def __init__(self, question):
#         '''
#
#         :param question:
#         '''
#         self.question = question
#         self.responses = []
#
#     def show_question(self):
#         '''
#         显示问卷
#         :return:
#         '''
#         print(self.question)
#
#     def store_response(self, new_response):
#         '''
#         存储单份调查问卷
#         :param new_response:
#         :return:
#         '''
#         self.responses.append(new_response)
#
#     def show_results(self):
#         '''
#         显示所有答卷
#         :return:
#         '''
#         print('Survey results:')
#         for response in self.responses:
#             print('- ' + response)
#
#
#
# import unittest
#
# class TestAnonmyousSurvey(unittest.TestCase):
#
#     def test_store_single_response(self):
#         '''
#         测试保存单份问卷的方法
#         :return:
#         '''
#         question = "世上最好的语言是？"
#         language_survey = AnonymousSurvey(question)
#         language_survey.store_response('php')
#
#         self.assertIn('php', language_survey.responses)
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()


import time
import multiprocessing

def doIt(num):
	print("Process num is : %s" % num)
	time.sleep(1)
	print('process  %s end' % num)
if __name__ == '__main__':
	# print('mainProcess start')
	# #记录一下开始执行的时间
	# start_time = time.time()
	# #创建三个子进程
	# pool = multiprocessing.Pool(3)
	# print('Child start')
	# for i in range(3):
	# 	pool.apply(doIt,[i])
	# print('mainProcess done time:%s s' % (time.time() - start_time))
	print('192.168.1.1,192.168.0.2'.split(','))
