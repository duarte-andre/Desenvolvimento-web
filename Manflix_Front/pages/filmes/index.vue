<script setup>

  const{data:filmesResult} = await useFetch(`http://localhost:8000/filmes`);

</script>

<template>
  <div>
      <div v-for="filmeValue in filmesResult" :key="filmeValue.id">
        <NuxtLink :to="'/filmes/'+filmeValue.id">
          <img :src="'http://localhost:8000'+filmeValue.banner" alt="">
        </NuxtLink>
        <h3>{{ filmeValue.nome }}</h3>    
        <br>  


      </div><br>

   
  </div>
</template>