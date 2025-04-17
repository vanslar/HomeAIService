<script setup>
import NavView from './Views/NavView.vue';
</script>

<template>
  <div class="common-layout">
    <el-container>
        <el-aside width="200px">
            <NavView />
        </el-aside>
        <el-container>
            <el-header>
              <h3 style="text-align: left; margin-left: 0;">Welcome To HomeAI</h3>
            </el-header>
            <el-main>
              <router-view />
            </el-main>
<!--
            <el-footer>
            </el-footer>
-->
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
</style>
