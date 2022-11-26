import { metadata } from '$lib/constants';

/** @type {import('./$types').LayoutLoad} */
export async function load() {
    return {
        title: metadata.name,
        data: []
    };
}
