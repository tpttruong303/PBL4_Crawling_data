<script lang="ts" setup>
import { ref, onBeforeMount, watch } from "vue";
import { updateInfo, getInfo } from "@/services/user.service";
import { IUpdate, ILogin } from "@/types/user";
import { ElNotification } from "element-plus";

onBeforeMount(async () => {
  await handleGetInfo();
});
const isArrowUp = ref(false);
const dataInfo = ref<ILogin>();

watch(dataInfo, (newValue) => {
  if (newValue) {
    updateI.value = {
      name: newValue.name || "",
      age: newValue.age || 0,
      avatar: newValue.avatar || "",
      email: newValue.email || "",
    };
  }
});
const handleGetInfo = async () => {
  try {
    const res = await getInfo();
    dataInfo.value = res["data"];
    console.log(dataInfo.value);
  } catch (error) {
    console.log(error);
  }
};
const updateI = ref<IUpdate>({
  name: dataInfo.value?.name,
  age: dataInfo.value?.age,
  avatar: dataInfo.value?.avatar,
  email: dataInfo.value?.email,
});
const handleUpdate = async () => {
  try {
    await updateInfo(updateI.value);
    ElNotification({
      title: "Success",
      message: "Update succesfully!",
      type: "success",
    });
  } catch (error) {
    ElNotification({
      title: "Error",
      message: "Update failed!",
      type: "error",
    });
    console.error(error);
  }
};

</script>
<template>
    <div class="grid">
        <div class="grid__row">
                    <div class="profile__container-title--img">
                        <div class="profile__container-title">
                            <h1>Tài khoản</h1>
                            <p>Hãy cập nhật thông tin mới nhất.</p>
                            <p>Thông tin cá nhân dưới đây sẽ tự động điền khi bạn tạo hồ sơ mới.</p>
                        </div>
                        <div class="profile__container-img">
                            <img :src="updateI.avatar" alt="avatar">
                        </div>
                    </div>
                    <ul class="profile__container-listgroup">
                        <li class="profile__container-listgroup--items">
                            <label>Họ và tên</label>
                            <input v-model="updateI.name" type="text">
                        </li>
                        <li class="profile__container-listgroup--items">
                            <label>Tuổi</label>
                            <input v-model="updateI.age" type="text">
                        </li>
                        <li class="profile__container-listgroup--items">
                            <label>Email đăng nhập</label>
                            <input v-model="updateI.email" type="text">
                        </li>
                    </ul>
                    <div class="button-edit-infor"><button @click="handleUpdate()"><el-icon><Edit /></el-icon><span> Cập nhật </span></button></div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.grid{
    margin: 0 auto;
    width: 1200px;
    max-width: 100%;
    margin-top: 110px;
}
.grid__row{
    display: flex;
    margin-right: -15px;
    margin-left: -15px;
    flex-wrap: wrap;
    justify-content: center;
    flex-direction: column;
}
.profile__container-title--img{
    display: flex;
    width: 100%;
    font-size: 17px;
    gap: 20%;
    justify-content: center;
}
.profile__container-title{
    padding-right: 1rem !important;
}
.profile__container-title h1{
    font-size: 1.75rem;
    margin-bottom: 0.5rem;
    font-weight: 700;
    line-height: 1.2;
    color: #00133F;
}
.profile__container-title p{
    color: #6c757d !important;
}
.profile__container-img img{
    width: 100px;
    height: 100px;
    border-radius: 100%;
}
.profile__container-img{
    display: flex;
    flex-direction: column;
    gap: 7px;
}
.profile__container-img input{
    border: 1px;
    background-color: white;
    cursor: default;
    font-size: 1.5rem;
}
.profile__container-listgroup{
    display: flex;
    flex-direction: column;
    padding-left: 0;
    margin-bottom: 0;
    margin-top: 1.5rem;
}
.profile__container-listgroup--items{
    display: flex;
    gap: 25%;
    padding: 0.75rem 1.25rem;
    color: #0E1225;
    background-color: #fff;
    border: 1px solid rgba(0,0,0,0.125);
    border-width: 0 0 1px;
    justify-content: center;
    margin: 20px 0;
}
.profile__container-listgroup--items label{
    font-size: 24px;
    width : 300px;
}
.profile__container-listgroup--items input{
    width: 300px;
}
.button-edit-infor button {
    padding: 7px 20px;
    background-color: #F1ECF6;
    border: none;
    border-radius: 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    margin-left: auto;
    margin-right: 80px;
}
.button-edit-infor button:hover {
    background-color: #afa8e0;
}
</style>