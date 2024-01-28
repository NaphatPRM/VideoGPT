import os
from resemble import Resemble
import requests
from dotenv import load_dotenv

load_dotenv()

api_key=os.environ.get("RESEMBLE_API_KEY")
Resemble.api_key(api_key)

class AudioAI:




    def generate(
        self,
        prompt,
        project_uuid='c01b4170',
        voice_uuid = '00b1fd4e',
        output_file="audio.wav",
    ):

        try:
            response = Resemble.v2.clips.create_sync(
                project_uuid,
                voice_uuid,
                prompt,
                is_public=False,
                is_archived=False,
                title=None,
                sample_rate=None,
                output_format=None,
                precision=None,
                include_timestamps=None,
                raw=None
            )
            print(response)
            if response['success']:
                clip = response['item']
                clip_uuid = clip['uuid']
                clip_url = clip['audio_src']

                async_audio_response = requests.get(clip_url)
                with open(output_file, 'wb') as async_audio_file:
                    async_audio_file.write(async_audio_response.content)

            # prediction = self.llm.predict_by_bytes(
            #     prompt.encode(), input_type="text", inference_params=inference_params
            # )
            # output_base64 = prediction.outputs[0].data.audio.base64
            # with open(output_file, "wb") as f:
            #     f.write(output_base64)
            # return True
        except Exception as e:
            print(e)
            return False

    def get_voice_ids(self):
        """
        Get the available voice IDs.

        Returns:
            dict: A dictionary containing the available voice IDs.
        """
        return self.voice_ids




if __name__ == "__main__":
    # from dotenv import load_dotenv

    # load_dotenv()
    audio_ai = AudioAI()
    audio_ai.generate(
        prompt="weather is very good today. let's go to the beach",
        output_file="audio.wav",
    )

