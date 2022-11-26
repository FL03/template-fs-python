<script>
    /** @type {import('./$types').PageData} */
    export let data;
    import { Editor, Viewer } from 'bytemd'
    import gfm from '@bytemd/plugin-gfm'
    import 'bytemd/dist/index.css';
    
    let value = '';
    let plugins = [gfm()]
  
    function handleChange(e) {
      value = e.detail.value
    }
  </script>
  
  <div class="flex flex-auto items-center justify-between py-24 min-h-full max-h-screen min-w-full max-w-screen">
    <Editor
        {value}
        on:change={(e) => {
        value = e.detail.value
        }}
        {plugins}
    />
  </div>