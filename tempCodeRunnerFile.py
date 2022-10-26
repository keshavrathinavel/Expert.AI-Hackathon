    # def combine_recordings_if_needed(self):
    #      """
    #      If recording was paused, combines all sections in alphabetical order into a new audio file
    #      """
    #      if self.section_count > 1:   # this is incremented when a recording is paused/resumed
    #          combined_audio = AudioSegment.empty()
    #          files_combined = []
    #          for rec in glob.glob(os.path.join(self.RECORDING_DIR, "*" + self.FILE_EXT)):
    #              combined_audio = combined_audio + AudioSegment.from_wav(rec) # this is why alphabetical order is important
    #              files_combined.append(rec)
    #          combined_file_name = os.path.join(self.RECORDING_DIR, self.base_filename + "_combined" + self.FILE_EXT)
    #          combined_audio.export(out_f=combined_file_name, format="wav")
    #          logger.info(f"Combined the following recordings into {combined_file_name}:"
    #                      f"\n {files_combined}")