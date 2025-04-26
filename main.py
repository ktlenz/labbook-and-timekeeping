"""Main function to generate the lab book"""

if __name__ == "__main__":
    import gradio as gr
    import datetime

    def get_timestamp():
        """
        Get the current timestamp in the format YYYY-MM-DD HH:MM:SS

        Returns:
            datetime: Current timestamp
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    demo = gr.Interface(
        fn=get_timestamp,
        inputs=["path",
                gr.Radio(['Started working',
                         'Stopped working']),
                'text'],
        outputs="text"
    )
    demo.launch()
