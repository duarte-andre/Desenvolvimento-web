<script setup>
    const{data:usuariosReceived}= await useFetch(`http://localhost:8000/usuarios/`);
</script>

<template>
    <main>
        <h1>Usuários</h1>
        <div v-for="userValues in usuariosReceived" :key="userValues.id">
            <NuxtLink :to="'/favoritos/'+userValues.id">
                <h3>Nome: {{ userValues.nome }}</h3>
            </NuxtLink>            
            <h3>Assinatura: {{ userValues.idAssinaturaFK.nome }}</h3>
            <h3>E-mail: {{ userValues.email }}</h3>
            <br>
        </div><br>
    </main>
</template>