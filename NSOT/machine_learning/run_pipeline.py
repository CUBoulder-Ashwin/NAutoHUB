from predict.llm_extract import real_llm_extract, process_cli_output
from predict.predict_specific import predict_specific_output
from predict.predict_genericshow import predict_generic_show_command
from helper.generate_show import generate_show_command
from helper.generate_config import render_device_config
from helper.fetch_show import connect_and_run_command


def run_pipeline(user_input):
    extracted_actions = real_llm_extract(user_input)

    if not extracted_actions:
        return

    for action in extracted_actions:
        intent = action.get('intent')
        device = action.get('device')
        monitor = action.get('monitor')
        configure = action.get('configure')

        if (configure is None or configure == {}) and monitor is None:
            print("\nGeneric Show Command Prediction...")

            if intent:
                cli_command = predict_generic_show_command(intent)
                print(f"\n CLI Command: {cli_command}")
                output = connect_and_run_command(device, cli_command)

                if output:
                    final_answer = process_cli_output(user_input, output)
                    print(f"\nLLM Final Answer:\n{final_answer}")

        elif (configure is None or configure == {}):
            print("\n Specific Show Command..")

            predicted_show_type = predict_specific_output(intent)
            print(f"\nThe predicted show type is : {predicted_show_type}")

            final_command = generate_show_command(predicted_show_type, monitor)

            if final_command:
                print(f"\n Final Show Command: {final_command}")
                output = connect_and_run_command(device, final_command)

                if output:
                    final_answer = process_cli_output(user_input, output)
                    print(f"\n LLM Final Answer:\n{final_answer}")

        elif monitor is None:
            print("\n Configuration mode...")

            # Predict the correct template based on intent
            predicted_output = predict_specific_output(intent)

            if not predicted_output.endswith('.j2'):
                #print(f"❌ Prediction Error: Expected a template file, but got '{predicted_output}'")
                return

            template_file = predicted_output

            # Example: parse known structure into dict
            params = {}  
            if isinstance(configure, dict):
                params = configure
            else:
                print("⚠️ Warning: config data not parsed properly. Using fallback.")
                params = {"raw": configure}

            # Render the final config using template
            config_text = render_device_config(device, template_file, params)

            if config_text:
                print(f"\n Final Config for {device}:\n{config_text}")


if __name__ == "__main__":
    print(" Starting continuous assistant. Type 'exit' to quit.\n")
    while True:
        user_query = input("Enter your query (or 'exit' to quit): ").strip()
        if user_query.lower() in ['exit', 'quit']:
            print("👋 Exiting pipeline. Goodbye!")
            break
        run_pipeline(user_query)
