import openai


def get_completion(prompt, model):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model, temperature, max_tokens):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # Mennyire random a válasz
        max_tokens=max_tokens,  # Max token kimenet
    )
    return response.choices[0].message["content"]


def get_completion_and_token_count(messages, model, temperature, max_tokens):

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    content = response.choices[0].message["content"]

    token_dict = {
        "prompt_tokens": response["usage"]["prompt_tokens"],
        "completion_tokens": response["usage"]["completion_tokens"],
        "total_tokens": response["usage"]["total_tokens"],
    }

    return content, token_dict
