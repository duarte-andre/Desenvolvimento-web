<template>
  <div class="container">
    <!-- Mensagem de boas-vindas -->
    <h1>Bem-vindo ao Sistema</h1>

    <!-- Imagem de Logo -->
    <img :src="logoUrl" alt="Logo" id="logo" />

    <!-- Seletor de E-mails -->
    <label for="emailSelect">Selecione um usuário:</label>
    <select v-model="selectedUserId" id="emailSelect">
      <option value="" disabled>Escolha um usuário</option>
      <option v-for="usuario in usuarios.data" :key="usuario.id" :value="usuario.id">
        {{ usuario.email }}
      </option>
    </select>

    <!-- Campo de Senha -->
    <label for="password">Senha:</label>
    <input type="password" v-model="password" id="password" :disabled="selectedUserId === ''" />

    <!-- Botão de Login com NuxtLink -->
    
    <NuxtLink :to="'/homepage/' + selectedUserId" v-if="selectedUserId !== '' && isPasswordCorrect">
      <button @click="login" :disabled="!isPasswordCorrect">Login</button>
    </NuxtLink>
  </div>
</template>

<script setup>
 definePageMeta({
      layout: 'login'
    })
import { ref, watchEffect } from 'vue';

// Dados do usuário
const usuarios = ref({
  data: [
    { id: 1, email: 'sss@sss.com', senha: 'senha1' },
    { id: 3, email: 'majmrs@gmail.com', senha: 'senha2' },
    { id: 4, email: 'andre@gmail.com', senha: 'senha3' },
    { id: 6, email: 'boss@boss.com', senha: 'senha4' },
  ],
});

// ID do usuário selecionado
const selectedUserId = ref('');

// URL da imagem do logo
    const logoUrl = 'https://imgs.search.brave.com/Mj64ir0ZmAtLD1my73lTr0vwcu0dJUksb2xd_IoukhU/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9sb2dv/ZG93bmxvYWQub3Jn/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDE0/LzA5L2dvb2dsZS1s/b2dvLTEucG5n';

// Senha digitada pelo usuário
const password = ref('');

// Verifica se a senha está correta
const isPasswordCorrect = ref(false);

// Função para validar a senha
const validatePassword = () => {
  const user = usuarios.value.data.find(user => user.id === parseInt(selectedUserId.value));
  isPasswordCorrect.value = user ? password.value === user.senha : false;

  
};

// Observador para validar a senha sempre que o ID do usuário ou a senha mudar
watchEffect(() => {
  validatePassword();
});

// Função para simular a ação de login
const login = () => {
  // Implemente a lógica de login aqui
  console.log(`Usuário logado com ID: ${selectedUserId.value}`);
};
</script>

<style>
.container {
  display: flex;
  position: relative;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  margin: auto;
  margin-top: 10%;
  width: 35%;
}

#logo {
  display: flex;
  width: 550px;
  height: auto;
}

#emailSelect {
  display: flex;
  width: 250px;
}

#password {
  display: flex;
  width: 250px;
}
</style>
