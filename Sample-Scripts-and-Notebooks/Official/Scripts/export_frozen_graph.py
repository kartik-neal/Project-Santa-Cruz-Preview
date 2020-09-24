"""
Exports a frozen graph from a model checkpoint so that we can use it to do evaluation.
"""
import argparse
import os
import subprocess


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modelpath", type=str, help="Path to the root of the Tensorflow Object Detection API repository.")
    parser.add_argument("checkpoint", type=str, default=None, help="Should be a /path/to/dir/chkpoint-prefix")
    parser.add_argument("config", type=str, help="Path to the TF Object Detection API configuration file to use.")
    parser.add_argument("--outputdpath", '-o', type=str, default=".", help="Location to output the frozen graph.")
    args = parser.parse_args()

    # Sanity check the args
    if not os.path.isdir(args.modelpath):
        print("Given a path to the TF object detection API root, but it does not point to a directory: {}".format(args.modelpath))
        exit(1)

    if not os.path.isfile(args.config):
        print("Given a path to a config file, but it does not point to a real file: {}".format(args.config))
        exit(2)

    chckpt_dpath = os.path.dirname(args.checkpoint)
    if not os.path.isdir(chckpt_dpath):
        print("Given a path to a checkpoint, but it does not seem to exist: {}. Specifically, cannot find {}".format(args.checkpoint, chckpt_dpath))
        exit(3)

    # Abspath everything
    modeldpath = os.path.abspath(args.modelpath)
    configfpath = os.path.abspath(args.config)

    # Adjust python path
    research = os.path.join(modeldpath, "research")
    slim = os.path.join(research, "slim")
    if 'PYTHONPATH' in os.environ:
        os.environ['PYTHONPATH'] += ":" + research + ":" + slim
    else:
        os.environ['PYTHONPATH'] = research + ":" + slim

    script = os.path.join(modeldpath, "research", "object_detection", "export_inference_graph.py")
    script_and_args = [
        "python3",
        script,
        "--input_type=image_tensor",
        "--pipeline_config_path={}".format(configfpath),
        "--output_directory={}".format(args.outputdpath),
        "--trained_checkpoint_prefix={}.".format(args.checkpoint),
    ]
    subprocess.run(script_and_args)
