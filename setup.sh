mkdir -p ~/.streamlit/

# shellcheck disable=SC2028
echo "\
[server]\n\
headless = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml