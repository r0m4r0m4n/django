<template>
  <li>
    <span v-bind:class="{done: item.completed}">
      <input type="checkbox" v-on:change="item.completed = !item.completed">
      <strong>{{ item.id }}</strong>
    {{ item.title }}
    </span>
    <button class="rm">&times;</button>
  </li>
</template>
<script>

export default {
  props: {
    item: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
  li {
    border: 1px solid #ccc;
    display: flex;
    justify-content: space-between;
    padding: .5rem 2rem;
    margin-bottom: 1rem;
  }

  .rm {
    background: red;
    color: #fff;
    border-radius: 50%;
    font-weight: bold;
  }
  input{
    margin-right: 1rem;
  }
  .done {
    text-decoration: line-through;
  }
  </style>