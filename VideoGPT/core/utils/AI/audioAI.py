import os
from resemble import Resemble
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("RESEMBLE_API_KEY")
Resemble.api_key(api_key)


class AudioAI:
    def generate(
        self,
        prompt,
        project_uuid="c01b4170",
        voice_uuid="00b1fd4e",
        output_file="audio.wav",
    ):
        try:
            project_uuid1 = "c01b4170"
            voice_uuid1 = "00b1fd4e"


            # project_uuid = "c01b4170",
            # voice_uuid = "00b1fd4e",
            # output_file = "audio.wav",
            response = Resemble.v2.clips.create_sync(
                project_uuid1,
                voice_uuid1,
                prompt,
                is_public=False,
                is_archived=False,
                title=None,
                sample_rate=None,
                output_format=None,
                precision=None,
                include_timestamps=None,
                raw=None,
            )
            # print(response)
            if response["success"]:
                clip = response["item"]
                clip_uuid = clip["uuid"]
                clip_url = clip["audio_src"]

                async_audio_response = requests.get(clip_url)
                with open(output_file, "wb") as async_audio_file:
                    async_audio_file.write(async_audio_response.content)

        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    audio_ai = AudioAI()
    audio_ai.generate(
        prompt="weather is very good today. let's go to the beach", output_file="audio1.wav"
    )
