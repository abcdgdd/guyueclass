#encoding:utf-8
import sys
from PyQt5.QtWidgets import  QApplication,QWidget
if __name__ == '__main__':
    #创建qt主程序类
    app = QApplication(sys.argv)
    #创建widge窗体
    w = QWidget()
    #设置窗名称
    w.setWindowTitle("hello word!!")
    #显示该窗体
    w.show()
    #阻塞主函数 等待APP退出
    sys.exit(app.exec_())
   
