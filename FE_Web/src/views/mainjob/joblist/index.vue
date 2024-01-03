<template>
  <div class="container-listjob">
    <div class="card-listjob" @click="toJobDetail(job.id)">
      <div class="img-card">
        <img :src="job.Image" alt="image" />
      </div>
      <div class="text-card">
        <h3 class="title">{{ job?.Title || "No Title" }}</h3>
        <p class="company">{{ job?.Company || "No Company" }}</p>
        <p class="location">{{ job?.Location || "No Location" }}</p>
        <span class="salary">{{ job?.Salary || "No Salary" }} |</span>
        <span>{{ job?.Level || "No Level" }}</span>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import type { IJob } from "../../../types/auth";
import { useRouter } from "vue-router";

const props = defineProps<{
  job: IJob;
}>();
const router = useRouter();
const toJobDetail = (idChoose: string) => {
  router.push(`/mainjob/${idChoose}`)
}
</script>
<style scoped>
.img-card img {
  width: 90px;
  height: 90px;
}
.img-card {
  float: left;
}
.card-listjob {
  display: grid;
  grid-template-columns: 100px auto;
  gap: 15px;
  background-color: #f5fcfe;
  padding: 30px 15px;
  border-radius: 15px;
  border: 1px solid rgb(2, 105, 219, 0.2);
  cursor: pointer;
}
.card-listjob:hover {
  transition: all 0.5s ease;
  box-shadow: 5px 5px 5px 0px rgb(2, 105, 219, 0.5);
}
.container-listjob {
  padding: 15px 25px;
}
.text-card .title{
  display: block;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
  color: #00133f;
}

.text-card .title:hover{
  text-decoration: underline;
}

.text-card .company {
  color: #343a40;
  font-size: 14px;
  padding-top: 3px;
  display: block;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
}
.text-card .location {
  color: #6c757d;
  font-size: 12px;
  padding-top: 3px;
  display: block;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
}
.text-card span {
  color: #6c757d;
  font-size: 12px;
  padding-top: 3px;
}
.salary {
  color: #4a9bef !important;
  font-weight: 600;
}
</style>
