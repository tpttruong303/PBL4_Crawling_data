<script setup lang="ts">
import { useRouter } from "vue-router"
import { ref } from "vue"
import { ILogin, } from "../../types/user"
import { loginApi } from "../../services/user.service"
import { initAuthStore } from '@/stores'
import { ElNotification } from "element-plus";

const user = ref<ILogin>({
    email: "",
    password: ""
})
const router = useRouter()
const submit = async () => {
    try {
        await loginApi({ email: user.value.email, password: user.value.password }).then((res) => {
            const data = res["data"]
            console.log(data.data.access_token)
            localStorage.setItem("access_token", data.data.access_token)
            localStorage.setItem("refresh_token", data.data.refresh_token)
        })
        await initAuthStore()
        router.push("/mainjob")
        ElNotification({
        title: "Thành công",
        message: "Đăng nhập thành công!",
        type: "success",
        });
    } catch (error) {
        ElNotification({
        title: "Thất bại",
        message: "Đăng kí thất bại, vui lòng kiểm tra lại!",
        type: "error",
        });
        console.log(error)
    }
};

</script>

<template>
    <div class="grid">
        <div class="grid__column-5">
            <div class="banner-container">
                <h1 class="banner-container__tittle">Xây dựng
                    <b>
                        sự nghiệp
                        <br>
                        <span class="banner-container__tittle__css">thành công!</span>
                    </b>
                </h1>
                <div class="banner-container__circle"></div>
                <img src="https://dxwd4tssreb4w.cloudfront.net/web/images/pages/login/banner.png" alt="Anh banner" class="banner-container__banner">
            </div>
        </div>
        <div class="grid__column-5">
            <div class="login-container">
                <div class="login-container__form">
                <h1 class="login-container__form__title">Đăng nhập bằng tài khoản của bạn</h1>
                <div class="login-container__form__content">
                <el-input v-model="user.email" placeholder="Email" class="login-container__form__content__input" />
                <el-input v-model="user.password" type="password" placeholder="Mật khẩu" show-password class="login-container__form__content__input" />
                <div class="login-container__form__content__co"></div>
                <el-button @click="submit" class="login-container__form__content__submit" type="primary">Đăng nhập</el-button>
                <div class="login-container__form__content__register">
                    <span>Chưa có tài khoản?</span>
                    <el-link type="primary" href="/register">Đăng ký</el-link>
                </div>
            </div>
        </div>
    </div>
        </div>
    </div>
    
</template>

<style lang="scss" scoped>
.grid {
    display: flex;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px;
}
.grid__column-5{
    padding-left: 5px;
    padding-right: 5px;
    width: 50%;
    background-color: #f9f9fa;
}
.banner-container{
    position: relative;
    width: 40vw;
    overflow: hidden;
    height: 116% !important;
    margin: auto !important;
}
.banner-container__tittle{
    font-size: 46px;
    font-weight: 300;
    padding: 0 60px;
}
.banner-container__banner{
    width: 80%;
    position: absolute;
    left: 10%;
    bottom: 0;
}
.banner-container__circle{
    background-color: #f7b500;
    width: 38vw;
    height: 38vw;
    border-radius: 50%;
    position: absolute;
    bottom: -25vw;
}
.banner-container__tittle{
    margin-top: 3rem !important;
}
.banner-container__tittle b{
    font-weight: 900;
}
.banner-container__tittle__css{
    color: #0069DB !important;
}
.login-container {
    width: 100%;
    height: 116%;
    overflow: hidden;
    background-color: #0069DB;
    &__form {
        width: 54%;
        margin: auto;
        margin-top: 100px;
        background: #fff;
        padding: 70px 20px 100px;
        border-radius: 12px;
        &__title {
            font-weight: 700;
            font-size: 1.5rem;
            line-height: 2rem;
            margin-bottom: 2rem;
            text-align: center;
        }
        &__content {
            padding: 0 30px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            &__co {
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 100%;
            }
            &__input,
            &__submit {
                width: 100%;
            }
            &__register {
                span {
                    font-size: 12px;
                    padding-right: 8px;
                }
            }
        }
    }
}
</style>
