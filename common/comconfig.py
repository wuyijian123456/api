#封装数据库操作：
import pymssql
class SqlServer:
    def _init_(self,host,port,username,password,db):
        self.host=host
        self.port=port
        self.username=username
        self.password=password
        self.db=db
    def get_connect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        #连接数据库
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur


    def ExecQuery(self, sql):  # 执行查询语句
        cur = self.get_connect()
        cur.execute(sql)
        data = cur.fetchall()  # 一次获取全部数据
        row = cur.fetchone()  # 一次获取一行数据
        rows = cur.fetchmany(10)  # 获取10行数据
        # 查询完毕后必须关闭连接
        self.conn.close()
        return data


    def ExecNonQuery(self, sql):  # 执行非查询语句
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

