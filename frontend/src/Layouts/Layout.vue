<template>
  <div class="common-layout">
    <el-container style="min-height: 100vh">
      <!-- 顶部导航栏 -->
      <el-header
        style="
          display: flex;
          align-items: center;
          border-bottom: 1px solid #ddd;
          background-color: #fff;
        "
      >
        <div
          style="flex: 1; display: flex; align-items: center; font-size: 24px; font-weight: bold"
        >
          <img style="width: 40px" src="@/assets/imgs/R-C.jpg" alt="" />
          <div style="margin-left: 10px">智能实验室预约系统</div>
        </div>
        <div>
          <el-dropdown>
            <div style="display: flex; align-items: center; cursor: pointer">
              <img src="@/assets/imgs/R-C.jpg" alt="" style="width: 30px; border-radius: 50%" />
              <div style="margin-left: 10px">管理员</div>
            </div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>
      <el-container>
        <!-- 侧边栏 -->
        <el-aside width="220px">
          <el-menu router style="height: 100%" default-active="/manager/home">
            <el-menu-item index="/manager/home">
              <el-icon><icon-menu /></el-icon>
              <span>系统首页</span>
            </el-menu-item>
            <el-menu-item index="/manager/lab">
              <el-icon><HomeFilled /></el-icon>
              <span>实验室管理</span>
            </el-menu-item>
            <el-menu-item index="/manager/equ">
              <el-icon><Tools /></el-icon>
              <span>设备列表管理</span>
            </el-menu-item>
            <el-menu-item index="/manager/user">
              <el-icon><UserFilled /></el-icon>
              <span>用户管理</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <!-- 主内容区域 -->
        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { HomeFilled, Menu as IconMenu, Tools, UserFilled } from '@element-plus/icons-vue'
import router from '@/router'

const logout = () => {
  router.push('/login')
}
</script>
