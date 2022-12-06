// import adapter from '@sveltejs/adapter-auto';

import adapter from '@sveltejs/adapter-node';
import adapter_vercel from '@sveltejs/adapter-vercel';
import preprocess from "svelte-preprocess";



const config = {
	kit: {
		...(process.env.MODE === "staging") && {
			adapter: adapter_vercel()
		},
		...(process.env.MODE !== "staging") && {
			adapter: adapter()
		}
	},
	preprocess: [
		preprocess({
			postcss: true,
		}),
	],
};

export default config;
