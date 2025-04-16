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
              header
            </el-header>
            <el-main>
              <div id="main" style="width: 600px;height:400px">main</div>
              main
            </el-main>
            <el-footer>
                Footer
            </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<style scoped>
</style>
