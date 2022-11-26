<script>
  /** @type {import('./$types').PageData} */
  export let data;
  import { Editor, Viewer } from 'bytemd'
  import gfm from '@bytemd/plugin-gfm'
  import 'bytemd/dist/index.css';
  
  let plugins = [gfm()]

  let value = data.content;
</script>


<Editor {plugins} {value} on:change={(e) => {value = e.detail.value}}/>