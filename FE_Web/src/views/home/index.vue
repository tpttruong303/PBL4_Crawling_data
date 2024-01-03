<script setup lang="ts">
import Header from "../../organisms/Header.vue";
import { useAuthStore } from "@/stores/auth";
defineProps<{}>();
const auth = useAuthStore();
</script>


<template>
  <Header />
  <div class="__default__ body-layout">
    <!-- <SearchComponent /> -->
    <slot class="body">
      
    </slot>
  </div>
</template>

<style lang="scss" scoped>
.body-layout {
  margin: 0 auto;
  width: 1300px;
  max-width: 100%;
  margin-top: 70px;
}
</style>
