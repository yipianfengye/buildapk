# coding=utf-8
import zipfile
import shutil
import os

# 创建一个空文件，此文件作为apk包中的空文件
src_empty_file = 'info/empty.txt'
f = open(src_empty_file,'w')
f.close()

# 在渠道号配置文件中，获取指定的渠道号
channelFile = open('./info/channel.txt','r')
channels = channelFile.readlines()
channelFile.close()
print('-'*20,'all channels','-'*20)
print(channels)
print('-'*50)

# 获取当前目录下所有的apk文件
src_apks = [];
for file in os.listdir('.'):
    if os.path.isfile(file):
        extension = os.path.splitext(file)[1][1:]
        if extension in 'apk':
            src_apks.append(file)

# 遍历所以的apk文件，向其压缩文件中添加渠道号文件
for src_apk in src_apks:
	src_apk_file_name = os.path.basename(src_apk)
	print('current apk name:',src_apk_file_name)
	temp_list = os.path.splitext(src_apk_file_name)
	src_apk_name = temp_list[0]
	src_apk_extension = temp_list[1]

	output_dir = 'outputDir'+'/'
	if not os.path.exists(output_dir):
		os.mkdir(output_dir)

	# 遍历从文件中获得的所以渠道号，将其写入APK包中
	for line in channels:
		target_channel = line.strip()
		target_apk = output_dir + 'mobile' + "-" + target_channel+"-release" + src_apk_extension
		shutil.copy(src_apk,  target_apk)
		zipped = zipfile.ZipFile(target_apk, 'a', zipfile.ZIP_DEFLATED)
		empty_channel_file = "META-INF/uuchannel_{channel}".format(channel = target_channel)
		zipped.write(src_empty_file, empty_channel_file)
		zipped.close()

print('-'*50)
print('repackaging is over ,total package: ',len(channels))



