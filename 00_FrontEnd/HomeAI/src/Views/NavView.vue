<script setup>
    import { ref } from 'vue'
    import {
        Document,
        Menu as IconMenu,
        Location,
        Setting,
        HomeFilled
    } from '@element-plus/icons-vue'

    const isCollapse = ref(true)
    const handleOpen = (key, keyPath) => {
    console.log(key, keyPath)
    }
    const handleClose = (key, keyPath) => {
    console.log(key, keyPath)
    }
</script>

<template>
<!--
  <el-radio-group v-model="isCollapse  " style="margin-bottom: 20px">
    <el-radio-button :value="!isCollapse">expand</el-radio-button>
  </el-radio-group>
-->
<!--
  <el-radio-button  v-model="isCollapse" @click="isCollapse=!isCollapse">
    <span>Collapse</span>
  </el-radio-button>
-->
<!--
  <el-menu
    default-active="2"
    class="el-menu-vertical-demo"
    :collapse="isCollapse"
    @open="handleOpen"
    @close="handleClose"
  >
-->
  <el-menu
    default-active="2"
    class="el-menu-vertical-demo"
    @open="handleOpen"
    @close="handleClose"
    router
  >
    <el-menu-item index="/HomeView">
      <el-icon><HomeFilled /></el-icon>
      <template #title>Home</template>
    </el-menu-item>
    <el-menu-item index="/HomeViewTest">
      <el-icon><HomeFilled /></el-icon>
      <template #title>HomeTest</template>
    </el-menu-item>




    <el-sub-menu index="1">
      <template #title>
        <el-icon><location /></el-icon>
        <span>Navigator One</span>
      </template>
      <el-menu-item-group>
        <template #title><span>Group One</span></template>
        <el-menu-item index="1-1">item one</el-menu-item>
        <el-menu-item index="1-2">item two</el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group title="Group Two">
        <el-menu-item index="1-3">item three</el-menu-item>
      </el-menu-item-group>
      <el-sub-menu index="1-4">
        <template #title><span>item four</span></template>
        <el-menu-item index="1-4-1">item one</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
    <el-menu-item index="2">
      <el-icon><icon-menu /></el-icon>
      <template #title>Navigator Two</template>
    </el-menu-item>
    <el-menu-item index="3" disabled>
      <el-icon><document /></el-icon>
      <template #title>Navigator Three</template>
    </el-menu-item>
    <el-menu-item index="4">
      <el-icon><setting /></el-icon>
      <template #title>Navigator Four</template>
    </el-menu-item>
  </el-menu>
</template>

<style scoped>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
    }
</style>