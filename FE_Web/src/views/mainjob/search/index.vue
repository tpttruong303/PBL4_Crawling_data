<template>
  <div>
    <div class="container-search">
      <div class="input-search">
        <input type="text" v-model="keySearch" placeholder="Nhập vị trị, công ty, từ khóa,..." />
      </div>
    </div>
    <div class="grid__row">
      <div class="grid__column-8">
          <div v-for="(job, index) in filteredJobs" :key="index">
            <JobList :job="job" />
          </div>
          <div class="pagination">
            <el-pagination
            background
            layout="prev, pager, next"
            :total="totalSearchedAndFilteredJobs"
            :page-size="pageSize"
            :current-page.sync="currentPage"
            @current-change="handlePageChange"
            />
          </div>
      </div>
      <div class="grid__column-10">
          <img src="https://www.careerlink.vn/images/common/vietcv-ad-tall-2x.png" class="container-banner" alt="VietCV">
          <img src="https://www.topcv.vn/images/banner/search-page/banner_surveyrecruitment_trend.png?v=2" class="container-banner" alt="TopCV">
      </div>
    </div>
    
  </div>
</template>
<script setup lang="ts">
import { ref, onBeforeMount, computed } from "vue";
import type { IJob } from "../../../types/auth";
import { getJobAll } from "../../../services/user.service";
import JobList from "../joblist/index.vue";

onBeforeMount(() => {
  getListJob();
});

const listJob = ref<Array<IJob>>([]);
const getListJob = async (): Promise<void> => {
  try {
    const res = await getJobAll();
    listJob.value = res.data;
    console.log(listJob.value);
  } catch (error) {
    console.log("error", error);
  }
};
const keySearch = ref("");
const pageSize = ref(10);
const currentPage = ref(1);
const totalSearchedAndFilteredJobs = computed(() => {
  return searchedAndFilteredJobs.value.length;
});
const filteredJobs = computed(() => {
  const start = (currentPage.value - 1) * pageSize.value;
  const end = start + pageSize.value;
  return searchedAndFilteredJobs.value
    .slice(start, end)
});
const searchedAndFilteredJobs = computed(() => {
  return listJob.value.filter((job) => {
    return (
      (job.Title.toLowerCase().includes(keySearch.value.toLowerCase())) ||
      (job.Location.toLowerCase().includes(keySearch.value.toLowerCase())) ||
      (job.Company.toLowerCase().includes(keySearch.value.toLowerCase())) ||
      (job.Salary.toLowerCase().includes(keySearch.value.toLowerCase())) ||
      (job.Level.toLowerCase().includes(keySearch.value.toLowerCase()))
    );
  });
});
const handlePageChange = (page: number) => {
  currentPage.value = page;
};
</script>
<style scoped>
.grid__row {
    display: flex;
    flex-wrap: wrap; /* độ dài vượt quá màn hình tự động xuống hàng*/
    margin-left: -5px;
    margin-right: -5px;
}
.container-search {
  display: flex;
  justify-content: center;
  padding: 40px 30px;
}

.grid__column-8{
    padding-left: 5px;
    padding-right: 5px;
    width: 66.6667%;
}

.grid__column-10{
    padding-left: 5px;
    padding-right: 5px;
    width: 33.333%;
}

.input-search input {
  padding: 5px 25px;
  outline: none;
  border-radius: 0.25rem;
  border: 1px solid #ced4da;
  width: 300px;
  height: 40px;
}
.select-province {
  display: flex;
  gap: 25px;
}
.select-province select {
  padding: 5px 25px;
  outline: none;
  cursor: pointer;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  color: #333;
  height: 40px;
}
.container-button button {
  padding: 5px 30px;
  background-color: #0069DB;
  border-color: #0069DB;
  color: #fff;
  border-radius: 0.25rem;
  border: 1px solid transparent;
  font-weight: 400;
  cursor: pointer;
  height: 40px;
}
.pagination {
  display: flex;
  justify-content: right;
  margin: 10px 0;
}

.container-banner{
  max-width: 100%;
  height: auto;
  margin: 15px 0;
}
</style>
